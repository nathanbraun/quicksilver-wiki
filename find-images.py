import os
import requests
import re
import time

def find_image_links(directory):
    # List to store all image links
    wiki_links = []

    # Regular expression pattern to find URLs ending in common image extensions inside parentheses
    img_pattern = re.compile(r'\((\/?https?:\/\/[^)]+?\.(?:jpg|jpeg|png|gif|bmp|svg))\)', re.IGNORECASE)

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            print(file)
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Search for image links in the file content
                    matches = img_pattern.findall(content)
                    for link in matches:
                        # Remove leading slash if present
                        if link.startswith('/'):
                            link = link[1:]
                        # Append the sanitized link to the wiki_links list
                        wiki_links.append(link)


    print(wiki_links)
    return wiki_links

def download_images(links, download_folder, sleep_time=0, skip=None):
    url_not_found = []  # List to store URLs that return a 404 error

    # Ensure the download folder exists
    os.makedirs(download_folder, exist_ok=True)
    
    for link in links:
        if skip is not None and link in skip:
            continue
        try:
            # Extract the image filename from the URL
            filename = os.path.basename(link)
            filepath = os.path.join(download_folder, filename)
            
            # Skip download if file already exists
            if os.path.exists(filepath):
                print(f"Skipped {filename}, already exists.")
                continue

            # Send a GET request to the image URL
            response = requests.get(link)
            response.raise_for_status()
            
            # Extract the image filename from the URL
            filename = os.path.basename(link)
            filepath = os.path.join(download_folder, filename)
            
            # Write the image content to a file
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"Downloaded {filename}")

            # Sleep for specified number of seconds
            time.sleep(sleep_time)
        
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Failed to download {link}: 404 Not Found")
                url_not_found.append(link)
        except Exception as e:
            print(f"Failed to download {link}: {e}")

    # Return the list of URLs that returned a 404 error
    return url_not_found

def replace_image_links(directory, images_folder):
    # Regular expression pattern to find URLs ending in common image extensions inside parentheses
    img_pattern = re.compile(r'(\(\/?https?:\/\/[^)]+?\/([^/]+\.(?:jpg|jpeg|png|gif|bmp|svg))\))', re.IGNORECASE)

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                
                # Read the Markdown file content
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Function to replace URLs with local paths
                def replace_link(match):
                    full_link = match.group(0)
                    filename = match.group(2)
                    new_link = f"(/images/{filename})"
                    return new_link

                # Replace links in the content
                new_content = img_pattern.sub(replace_link, content)

                # Write back the modified content to the Markdown file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                print(f"Processed {filepath}, links replaced.")

image_links = find_image_links('raw')
download_folder = 'docs/images'
not_found = download_images(image_links, download_folder, sleep_time=30)

not_found2 = download_images(image_links, download_folder, sleep_time=30,
                             skip=not_found)

not_found_all = not_found + not_found2

not_found3 = download_images(image_links, download_folder, sleep_time=30,
                             skip=not_found_all)


replace_image_links('docs', 'docs/images')
