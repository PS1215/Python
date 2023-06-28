import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import asyncio
import websockets

class ChatApp(App):
    def build(self):
        self.contacts = ['Piyush', 'Kusum', 'Tanu','Vivek','Anshul']
        self.selected_contact = self.contacts[0]
        
        # Connect to SQLite database
        self.conn = sqlite3.connect('chat.db')
        self.cursor = self.conn.cursor()
        self.create_table()
        
        layout = BoxLayout(orientation='vertical')
        
        self.chat_label = Label(text='Chat Messages with {}'.format(self.selected_contact))
        layout.add_widget(self.chat_label)
        
        self.contact_dropdown = DropDown()
        for contact in self.contacts:
            btn = Button(text=contact, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.select_contact(btn.text))
            self.contact_dropdown.add_widget(btn)
        
        contact_button = Button(text='Select Contact')
        contact_button.bind(on_release=self.contact_dropdown.open)
        layout.add_widget(contact_button)
        
        self.message_label = Label(text='Enter Message:')
        layout.add_widget(self.message_label)
        
        self.message_input = TextInput(multiline=False)
        layout.add_widget(self.message_input)
        
        send_button = Button(text='Send')
        send_button.bind(on_release=self.send_message)
        layout.add_widget(send_button)
        
        asyncio.ensure_future(self.receive_messages())
        
        return layout
    
    def select_contact(self, contact):
        self.selected_contact = contact
        self.chat_label.text = 'Chat Messages with {}'.format(self.selected_contact)
        self.contact_dropdown.dismiss()
        
        self.load_messages_from_db()
    
    def send_message(self, instance):
        message = self.message_input.text
        sender_message = '{}: {}'.format(self.selected_contact, message)
        self.insert_message_to_db(sender_message)
        self.message_input.text = ''
        
        asyncio.ensure_future(self.send_message_to_server(sender_message))
    
    def update_chat_label(self):
        self.chat_label.text = '\n'.join(self.messages)
    
    async def receive_messages(self):
        uri = "ws://localhost:8000"  # Replace with your server's WebSocket URI
        
        async with websockets.connect(uri) as websocket:
            while True:
                received_message = await websocket.recv()
                self.handle_received_message(received_message)
    
    def handle_received_message(self, message):
        # Extract sender and message from received message
        sender, received_message = message.split(":")
        sender_message = '{}: {}'.format(sender, received_message)
        
        self.insert_message_to_db(sender_message)
        
        if self.selected_contact == sender:
            self.messages.append(sender_message)
            self.update_chat_label()
    
    async def send_message_to_server(self, message):
        uri = "ws://localhost:8000"  # Replace with your server's WebSocket URI
        
        async with websockets.connect(uri) as websocket:
            await websocket.send(message)
    
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            contact TEXT,
                            message TEXT)''')
    
    def insert_message_to_db(self, message):
        self.cursor.execute("INSERT INTO messages (contact, message) VALUES (?, ?)",
                            (self.selected_contact, message))
        self.conn.commit()
    
    def load_messages_from_db(self):
        self.cursor.execute("SELECT message FROM messages WHERE contact = ?", (self.selected_contact,))
        result = self.cursor.fetchall()
        self.messages = [row[0] for row in result]
        self.update_chat_label()
    
    def on_stop(self):
        self.conn.close()
        asyncio.get_event_loop().stop()


if __name__ == '__main__':
    ChatApp().run()
