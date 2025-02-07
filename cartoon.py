import images
import wikipedia
import cv2

from images import get_wikipedia_page_thumbnail_url, download_image_from_url

def prompt_for_image():
    """
    Prompts the user for the name of a Wikipedia page and obtains the URL of the thumbnail image of the page.
    
    return url, page_name: str, str
    """
    search_query = input("Enter name of a personality: ")
    try:
        w_search = wikipedia.search(search_query, results=3)
        celeb = int(input(f"Select a name from the following list:\n1. {w_search[0]}\n2. {w_search[1]}\n3. {w_search[2]}\nEnter the number of the desired name: "))
        image = images.get_wikipedia_page_thumbnail_url(w_search[celeb-1])
        return image
    except Exception as e:
        print(f"Error: Unable to find image for the given name: {e}")
        return None, None
    
def convert_image_to_cartoon(image_path):
    """
    Converts an image to a cartoon given the image_path.
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(img, 9, 200, 200)
    cartoon = cv2.bitwise_and(color, color, mask = edges)
    cv2.imwrite(image_path, cartoon)

    
if __name__ == "__main__":
    image = prompt_for_image()
    convert_image_to_cartoon(image)

