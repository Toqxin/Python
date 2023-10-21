import requests

def get_streamer_info():

    client_id = 'client_id'
    client_secret = 'client_secret'
    channel_name = input('Twitch Channel Name:')
    
    token_url = 'https://id.twitch.tv/oauth2/token'
    token_payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    
    token_response = requests.post(token_url, data=token_payload)

    if token_response.status_code == 200:
        access_token = token_response.json()['access_token']
        channel_info_url = f'https://api.twitch.tv/helix/users?login={channel_name}'
        headers = {
            'Client-ID': client_id,
            'Authorization': f'Bearer {access_token}'
        }
        
        channel_info_response = requests.get(channel_info_url, headers=headers)
        
        if channel_info_response.status_code == 200:
            channel_data = channel_info_response.json()

            if channel_data['data']:
                channel_info = channel_data['data'][0]
                print('-'*150)
                print(f"🢅 Channel Name: {channel_info['display_name']}")
                print('-'*150)
                print(f"🢅 Channel ID: {channel_info['id']}")
                print('-'*150)
                print(f"🢅 Channel Created At: {channel_info['created_at']}")
                print('-'*150)
                print(f"🢅 Broadcaster Type: {channel_info['broadcaster_type']}")
                print('-'*150)
                print(f"🢅 Description: {channel_info['description']}")
                print('-'*150)
                print(f"🢅 Channel Profile Img: {channel_info['profile_image_url']}")
                print('-'*150)
                
                channel_id = channel_info['id']
                viewer_count_url = f'https://api.twitch.tv/helix/streams?user_id={channel_id}'
                viewer_count_response = requests.get(viewer_count_url, headers=headers)
                
                if viewer_count_response.status_code == 200:
                    viewer_count_data = viewer_count_response.json()

                    if viewer_count_data['data']:
                        viewer_count = viewer_count_data['data'][0]['viewer_count']
                        print(f'🢅 Now Live🔴 {viewer_count}')
                        print('-'*150)
                    
                    else:
                        print("The channel is not live right now.")
                else:
                    print("Live viewer count could not be obtained.")
            else:
                print("Channel not found.")
        else:
            print("Unable to retrieve channel information.")
    else:
        print("Access Token could not be received.")

if __name__ == "__main__":
    get_streamer_info()
