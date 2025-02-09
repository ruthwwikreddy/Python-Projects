import instaloader

class InstaInfoScraper:

    def __init__(self):
        # Create an instance of Instaloader class
        self.loader = instaloader.Instaloader()

    def getinfo(self, username):
        try:
            # Load the profile using the provided username
            profile = instaloader.Profile.from_username(self.loader.context, username)
            
            # Extracting details
            user = profile.full_name
            followers = profile.followers
            following = profile.followees
            posts = profile.mediacount
            email = profile.external_url  # Instagram does not provide email; external URL might be available

            print(f'User: {user}')
            print(f'Followers: {followers}')
            print(f'Following: {following}')
            print(f'Posts: {posts}')
            print(f'External URL (possibly email): {email}')
            print('---------------------------')
        
        except instaloader.exceptions.ProfileNotExistsException:
            print(f'Profile "{username}" does not exist.')

    def main(self):
        usernames = ['chanakya_bysani08']

        for username in usernames:
            self.getinfo(username)


if __name__ == '__main__':
    obj = InstaInfoScraper()
    obj.main()
