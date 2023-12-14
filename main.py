from telethon.sync import TelegramClient
from telethon.tl import functions, types, channels
import time, random, asyncio, os


api_id = 'yor_api'
api_hash = 'yor_api'
group_username = 'your group'
emojis = ['❤️', '👍', '🥰', '🔥'] # put here your emojis

async def react_to_messages(phone_number):
    
    client = TelegramClient(f'sessions/{phone_number}', api_id, api_hash)
    await client.start()
    await client(channels.JoinChannelRequest(group_username))
    try:
        messages = await client.get_messages(group_username, limit=100)

        for message in messages:
        
            await asyncio.sleep(0.2)
            emoji  = random.choice(emojis)
            if random.randint(1,2) == 2 and isinstance(message.media, types.MessageMediaPhoto):
                result = await client(functions.messages.SendReactionRequest(
                    peer=group_username,
                    msg_id=message.id,
                    big=True,
                    add_to_recent=True,
                    reaction=[types.ReactionEmoji(
                        emoticon=emoji
                    )]
                ))
                print(f' {emoji} adicionada à mensagem ID {message.id} com {phone_number}')
                await asyncio.sleep(0.2)
            else:
                await asyncio.sleep(0.1)
    except Exception as e:
        print(e)
    finally:    
        await client.disconnect()

async def main():
    sessoes_na_pasta = [session.replace('.session', '') 
                for session in os.listdir('sessions') if session.endswith('.session')]
    
    for phone_number in sessoes_na_pasta:
        await react_to_messages(phone_number)
    
asyncio.run(main())


