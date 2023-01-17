
# Project Introduction
With stock trading becoming easier and cryptocurrencies on the rise, more and more people are likely 
to engage in stock or cryptocurrency trading. As it stands now, people have to create an investment/brokerage 
account and set aside capital to actually start trading. As a result, this leads to a lot of financial risk if 
someone is naïve or has no experience. So **Wall Street Hero** allows people to learn important information about potential stocks, 
including price, market cap, volume, 52 week high price, etc. **Wall Street Hero** will potentially provide suggestions on whether 
a particular stock is a good buy or not. We aim to provide a simplistic UI/UX in order to help beginner investors not be overwhelmed 
by massive amounts of information in their investing journey. For example, Robinhood appeals to a younger audience due to its 
modern and simple UI/UX.

# Features
- Custom Login & SSO (Google)
- Get stock information
- Get company insight
- Get trending tickers
- Get top gainers/losers
- Get sector performance
- Get stock rating
- Get stock mentions on Reddit
- Get real time stock price (Amazon Lex Chatbot)
- Add / Update ticker
- Get market hours
- Get charts
- Get stock news
- Get similar stocks

# Sample Demo Screenshots
![Login](https://user-images.githubusercontent.com/2999334/143333136-418ea746-3551-42a5-be90-012a1f20ba1a.PNG)
![Home](https://user-images.githubusercontent.com/2999334/143333138-c5558ed8-fea2-4741-acd8-c945c9a814c6.PNG)
![Chatbot](https://user-images.githubusercontent.com/2999334/143333143-bbe89fc5-0e70-490b-ae9e-512fd35bed78.PNG)
<img width="1361" alt="Screen Shot 2021-11-24 at 4 51 52 PM" src="https://user-images.githubusercontent.com/2999334/143333192-4ad8b44b-a97d-4af5-a8ac-83e78cca570c.png">
<img width="1094" alt="Screen Shot 2021-11-24 at 4 52 09 PM" src="https://user-images.githubusercontent.com/2999334/143333194-bd6c7e90-e9dc-4ab8-a764-b42c47d8ab8d.png">



# Pre-requisites Set Up

To setup the backend :

cd stockapi/
python3 -m venv venv
pip3 install --upgrade pip
pip3 install -r requirements.txt
pip3 install yfinance --upgrade --no-cache-dir

To setup Frontend :

cd materialui
npm install 

# How to set up and run project locally?

Run backend :
cd stockapi/
startup_script_local.sh
servers starts at port 8080

Run frontend 
cd materialui 
npm start 
server starts at port 3000
