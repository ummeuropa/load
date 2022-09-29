import os, shutil, requests
from urllib.parse import unquote

def __build_headers(url: str, custom_headers: dict = None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
        "Accept": "*/*",
        "Accept-Encoding": "*",
        "Referer": url + ("/" if not url.endswith("/") else ""),
        "Origin": url,
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache" }

    if custom_headers is not None:
        for k, v in custom_headers.items():
            headers[str(k)] = str(v)
    
    return headers

def http_download ( url: str, output_folder: str, custom_headers: dict = None,
                    filec = 0, counter = 0, verbose: bool = False ):

    # --- Parse url, filename and output path --- #
    url = unquote(url)
    filename = url.split('/')[-1].split('?')[0]
    output = output_folder + '/' + filename

    # --- Check for existing files --- #
    if os.path.exists(output): 
        print(f"\t\t\033[31;1m{filename}\033[0m already exits! Skipping...")
        return
    
    # --- Create folder if it doesn't exist --- #
    if not os.path.exists(output_folder): os.mkdir(output_folder)

    # --- Get url and download media --- #
    headers = __build_headers(url, custom_headers)
    with requests.get(url, headers=headers, stream=True) as response:
        
        # --- Catch Errors --- #
        if response.status_code in (403, 404, 405, 500):
            print(f"033[31;1mError {response.status_code}:\033[0m download failed.")
            return

        # --- Download file --- #
        with open(output, 'wb+') as stream:
            if verbose:
                print(f"{counter}/{filec}\t{int(counter/filec*100)}%\tDownloading {filename}")
            shutil.copyfileobj(response.raw, stream)
    response.close()