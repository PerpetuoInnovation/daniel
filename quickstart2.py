from instapy import InstaPy
import schedule
import time

insta_username = 'journeyer'
insta_password = 'girlsgeneration2'

def job():
    try:
        session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=True, bypass_suspicious_attempt=True)
        session.login()
        session.unfollow_users(amount=20, onlyNotFollowMe=True, sleep_delay=60)
        session.set_upper_follower_count(limit=2500)
        session.set_lower_follower_count(limit = 10)
        session.set_user_interact(amount=2, randomize=True, percentage=50, media='Photo')
        session.set_do_follow(enabled=True, percentage=70)
        session.set_do_like(enabled=True, percentage=70)
        session.set_comments(['wow', 'nice colors', 'beautiful'])
        session.set_do_comment(enabled=True, percentage=80)
        session.interact_user_followers(['graysdir','natgeo','ocean','youngadventuress','mmuheisen','patrickwitty','TIME'], amount=1000, randomize=True)
        session.like_by_tags(['wanderlust', 'photography', '35mm'], amount=100)
        session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)

    except:
        import traceback
        print(traceback.format_exc())

schedule.every().day.at("3:24").do(job)
schedule.every().day.at("15:28").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)