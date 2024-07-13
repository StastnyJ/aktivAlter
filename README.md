This directory contains the AKTIVALTER chatbot we created for the Tech Challenge class at TUM. 

# How to install and run

## Hosting BOT API

To host the chatbot, you will need a server with a public IP address. It could be a physical server, Raspberry PI, or VPS hosted by any provider, such as DigitalOcean, AWS, Heroku, or Contabo. This tutorial is written for Linux servers, but any other system should also be possible.

First, you need to install Python3 and PIP3 on your server using the following commands.

```sh
sudo apt update
sudo apt install python3
sudo apt install python3-pip
```

To test the installation, you can use

```sh
python3 --version
pip3 --version
```

Now, clone the repository, go to the cloned repository folder and install all the required Python packages using the command

```sh
pip3 install -r requirements.txt
```

And start the application with the command

```sh
python3 app.py
```

or

```sh
nohup python3 app.py &
disown -h
```

to keep it running in the background after logging out of the server. Make sure that no other application is running on port 8099 and that the firewall is turned off or allows all communication on this port.

Now the API is running. To test it, you can go to the address `http://<your_ip_address>:8099/` in any browser and see message `Aktiv aelter chat bot API` on your screen. From now on, the chatbot will receive messages with POST requests on the address `http://<your_ip_address>/whatsapp`.

## Creating a Twillo account

You need to create an account on the Twillo platform [https://www.twilio.com/en-us](https://www.twilio.com/en-us). After registering and logging in to the Twillo website, go to the `Messaging > Try it out > Send a WhatsApp message` in the left menu. Now go to the `Sandbox settings` and fill `http://<your_ip_address>/whatsapp` to the *When a message comes in* textbox and select a POST method. In this way, you connect the running chatbot with the Twillo account. The second textbox asking about the status leave blank.

Now everything should be set up and you can contact the chatbot with phone number and join message displayed in the `Sandbox` tab on the same Twillo page.
