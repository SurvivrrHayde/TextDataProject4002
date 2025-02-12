import requests
import csv
import time
from bs4 import BeautifulSoup

# Headers to mimic a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Function to scrape reviews for a single movie
def scrape_reviews(movie_id, max_pages=5):
    url = f"https://www.imdb.com/title/{movie_id}/reviews/?ref_=tt_ov_ql_2&sort=submission_date%2Casc&spoilers=EXCLUDE"
    all_reviews = []

    for page in range(1, max_pages + 1):
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to retrieve page {page} for {movie_id}. Status code: {response.status_code}")
            break

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find review containers
        review_containers = soup.find_all('div', class_='ipc-html-content-inner-div')

        # Extract review text (first 25 per page)
        reviews = [review.get_text(strip=True) for review in review_containers[:25]]

        # Store results
        for review in reviews:
            all_reviews.append([movie_id, review])

        print(f"Scraped {len(reviews)} reviews from page {page} for {movie_id}.")

        # IMDb paginates using a "Load More" button (if applicable)
        load_more = soup.find('div', class_='load-more-data')
        if load_more:
            url = f"https://www.imdb.com{load_more['data-ajaxurl']}"
        else:
            break

        time.sleep(2)  # Avoid getting blocked

    return all_reviews


# Function to load movie IDs from a text file
def load_movie_ids(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


# Scrape reviews for all movies
def main():
    movie_ids = load_movie_ids("movie_ids.txt")
    all_reviews = []

    for movie_id in movie_ids:
        reviews = scrape_reviews(movie_id)
        all_reviews.extend(reviews)

    # Save all reviews to CSV
    csv_filename = "imdb_reviews.csv"
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["movie_id", "review_text"])
        writer.writerows(all_reviews)

    print(f"Saved {len(all_reviews)} reviews to {csv_filename}.")


if __name__ == "__main__":
    main()
