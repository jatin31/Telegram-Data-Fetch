import os
import pandas as pd
from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

#(https://my.telegram.org/auth?to=apps) register your number and get keys and hash
#when the client starts it demands mobile number Format(+(country_code)(yoiur mobile number)). After that enter the otp code
api_id = ''#put id and remove inverted commas
api_hash = ''#put api hash in inverted commas
client = TelegramClient('sess_name', api_id, api_hash)
client.start()
        
def getChats(channel_name):

        schat=[]
        chat_hist = client.get_messages(str(channel_name),100)
        for i in range(len(chat_hist)):
            if chat_hist[i].to_dict()['_'] == 'Message':
                temp = chat_hist[i].to_dict()
                list1=[]
                list1.append(temp['date'])
                list1.append(temp['from_id'])
                list1.append(temp['id'])
                list1.append(temp['message'])
                list1.append(temp['reply_to_msg_id'])
                list1.append(temp['via_bot_id'])
                schat.append(list1)
        return schat
    
def getParticipants(channel_name):
    
        spart=[]
        total_participants = client.get_participants(str(channel_name),aggressive=True)
        for i in range(len(total_participants)):
            if total_participants[i].to_dict()['_'] == 'User':
                temp = total_participants[i].to_dict()
                tlist=[]
                tlist.append(temp['username'])
                tlist.append(temp['first_name'])
                tlist.append(temp['last_name'])
                spart.append(tlist)
        return spart
    
def getParticipantInfo(id):
        
        return client.get_entity(id).to_dict()
    
def sendMessage(name):
        
        client.send_message('Group_name',message='your_message')

if __name__ == "__main__": 
     #getting chats of that channel
    channel_name = str(input("Enter the channel name::::"))
    chat = getChats(channel_name)
    #putting it in dataframe and get a csv file out of it
    col =['DateTime','From_Id(SendersId)','Message_id','Message','Reply_to_msg_id','Via_bot_id']
    chatDataFrame = pd.DataFrame(chat,columns=col)
    chatDataFrame.to_csv('Chats.csv',encoding='utf-8')
    
    #getting participants of that channel
    channel_name = str(input("Enter the channel name::::"))
    part = getParticipants(channel_name)
    #putting it in dataframe and get a csv file out of it
    col1 =['Username','First_Name','Last_Name']
    partDataFrame = pd.DataFrame(part,columns=col1)
    partDataFrame.to_csv('Participants.csv',encoding='utf-8')
    
    #other functions can be called according to need(telegram_id is an integer)