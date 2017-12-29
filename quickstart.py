from instapy import InstaPy

insta_username = 'journeyer'
insta_password = 'girlsgeneration2'

# set headless_browser=True if you want to run InstaPy on a server
try:
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=False, bypass_suspicious_attempt=True)
    session.login()
    session.unfollow_users(amount=10, onlyNotFollowMe=True, sleep_delay=60)
    # settings
    session.set_upper_follower_count(limit=2500)
    session.set_lower_follower_count(limit = 10)
    session.set_user_interact(amount=2, randomize=True, percentage=50, media='Photo')
    session.set_do_follow(enabled=True, percentage=70)
    session.set_do_like(enabled=True, percentage=70)
    session.set_comments(['wow', 'nice colors', 'beatufiul'])
    session.set_do_comment(enabled=True, percentage=80)
    session.interact_user_followers(['graysdir','natgeo','ocean','268_bea','ketszazhuszfelett','do.wa62','youngadventuress','jackiegreaney'], amount=1000, randomize=True)
    session.like_by_tags(['wanderlust', 'photography', '35mm'], amount=100)
    session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)


finally:
    # end the bot session
    session.end()
