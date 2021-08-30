token= 'EAACwLQLxclMBAC1umOrmmGadNeLYfNaK1UeZBaXB2ZAZA1AZBf1jzDRaJ5MPA9LEdA9cUyGK3ssjGFcWzMyCXioMJddLU6ZC9IajDmcSZC4ZAdaoxp7puPPhAe86HDUgT0saxJTjlK62ALWSaNUYq0cfZCif5bJo1fGZBmWfZAZCrDTz4x3z2ZBhgAZAH'
from pyfacebook import GraphAPI
import requests
graph = GraphAPI(access_token=token)
# api = GraphAPI(app_id="id", app_secret="secret", application_only_auth=True)

# graph.get_object(object_id="542529356981839")
print('hello')
link  = f"https://graph.facebook.com/542529356981839/feed?access_token={token}"

rq = requests.get(link)
print(rq.json())

