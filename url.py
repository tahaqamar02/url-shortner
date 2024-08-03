import pyshorteners

def shorten_url(service, long_url, api_key=None):
    s = pyshorteners.Shortener(api_key=api_key) if api_key else pyshorteners.Shortener()
    
    if service == 'tinyurl':
        return s.tinyurl.short(long_url)
    elif service == 'bitly':
        return s.bitly.short(long_url)
    elif service == 'isgd':
        return s.isgd.short(long_url)
    elif service == 'osdb':
        return s.osdb.short(long_url)
    else:
        raise ValueError(f"Service '{service}' is not supported")

if __name__ == "__main__":
    while True:
        long_url = input("Enter the long URL: ")
        service = input("Enter the service (tinyurl, bitly, isgd, osdb): ").lower()
        api_key = None
        
        if service == 'bitly':
            api_key = input("Enter your Bitly API key: ")

        try:
            short_url = shorten_url(service, long_url, api_key)
            print("Shortened URL:", short_url)
        except ValueError as e:
            print(e)
        
        continue_choice = input("Do you want to shorten another URL? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Exiting the URL shortener. Goodbye!")
            break
