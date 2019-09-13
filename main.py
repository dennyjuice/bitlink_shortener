import argparse
import requests
import os

from dotenv import load_dotenv

def cut_link(token, url):
  bitly_auth = {"Authorization": "Bearer {}".format(token)}
  json_data = {"long_url": url}

  response = requests.post('https://api-ssl.bitly.com/v4/shorten', json=json_data, headers=bitly_auth)
  response.raise_for_status()

  short_link = response.json()

  return short_link['id']

def count_clicks(token, link):
  bitly_auth = {"Authorization": "Bearer {}".format(token)}
  json_data = {"units": -1}

  response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary', json=json_data, headers=bitly_auth)
  response.raise_for_status()

  clicks = response.json()

  return clicks['total_clicks']

if __name__ == "__main__":

  load_dotenv()
  parser = argparse.ArgumentParser(
    description='Сокращение ссылки через bit.ly, либо вывод кол-ва кликов по битлинку'
  )
  parser.add_argument('user_link', help='Ссылка или битлинк')
  args = parser.parse_args()

  if args.user_link.startswith('bit.ly'):
    try:
      total_clicks = count_clicks(os.getenv("BITLY_TOKEN"), args.user_link)
      print(f"По вашей ссылке прошли {total_clicks} раз(а)")
    except requests.exceptions.HTTPError:
      print('Вы ввели неверную ссылку')
  else:
    try:
      print("Битлинк: ", cut_link(os.getenv("BITLY_TOKEN"), args.user_link))
    except requests.exceptions.HTTPError:
      print('Вы ввели неверную ссылку')