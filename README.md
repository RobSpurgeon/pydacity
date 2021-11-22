# pydacity
Hooking Audacity tone generator up to twitch chat


To set it up, fill in the username, token, client ID and channel with the appropriate values. You will need to go through twitch API to get the auth codes to get it to work
start up audacity, create five empty channels
go into Edit > Preferences > Modules > mod-script-pipeline:enabled to allow pydacity to access the program
run "python chatbot.py" once audacity is started up

At this point, the chatbot will process commands entered into the chatroom
The project will work whether you're streaming or not, but it will be more fun if you're streaming.


commands are listed in main.py
