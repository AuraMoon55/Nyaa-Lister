import requests
from bs4 import BeautifulSoup as bs
from . import db

nyaadb = db.logs


def get_magnet(url):
  r = requests.get(url)
  sp = bs(r.content, "html.parser")
  sp = sp.find_all("a", attrs={"class":"card-footer-item"})
  return sp[0].get("href")


def get_feed():
  r = requests.get("https://nyaa.si/?page=rss")
  sp = bs(r.content, "html.parser")
  item = sp.find_all("item")
  fex = []
  
  for sex in item:
    sex = str(sex).replace(">", " ")
    fex.append(sex.replace("<", "\n"))
  
  tits = []
  
  for z in fex:
    z = z.splitlines()
    for d in z:
      if "nyaa:" in d:
        a = d.replace("nyaa:", "")
        z.remove(d)
        a = a.split(" ", maxsplit=1)
        a = "= ".join(x for x in a)
        z.append(a)
      if d.startswith("/"):
        try:
          z.remove(d)
        except:
          pass
      if d.startswith("item"):
        z.remove(d)
      if "/nyaa:" in d:
        z.remove(d)
      if "/description" in d:
        z.remove(d)
    pr = "\n".join(a for a in z)
    pr = pr.replace("/description", "")
    pr = pr.replace('guid ispermalink="true"', 'View = ')
    pr = pr.replace("link/", "Link=")
    pr = pr.replace("title", "Title=")
    pr = pr.replace("pubdate", "Upload Time = ")
    pr = pr.split("\n\n")[1:]
    magnet = get_magnet(pr[1].split("View = ", maxsplit=1)[1])
    pr1 = pr[:3]
    pr2 = pr[13:]
    px = pr1 + pr2
    Dk = [x for x in px]
    Dk.pop(-2)
    zk = Dk[-1]
    sk = Dk[-2]
    Dk.pop(-2)
    Dk.pop(-1)
    sk = sk.splitlines() + zk.splitlines()
    Dk.append(sk[0])
    Dk.append(sk[6])
    Dk.append(sk[7])
    Dk.append(f"Magnet =\n{magnet}")
    Fuck = "\n\n".join(a for a in Dk)
    Hng = []
    Streak = Fuck.split('\n\n')
    for a in Streak:
      fr = a.split("=", maxsplit=1)
      fr = f"{fr[0]} = {fr[1]}"
      Hng.append(fr)
    Fuck = "\n\n".join(x for x in Hng)
    tits.append(Fuck)
  return tits


async def save_latest(anime):
  jso = {
    "anime": anime
  }
  z = get_latest()
  await nyaadb.delete_one({"anime"} z)
  return await nyaadb.insert_one(jso)

async def get_latest():
  x = await nyaadb.find()
    return x["anime"]
