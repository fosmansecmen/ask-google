# Ask Google
A simple app that 
- takes the question with a voice record,
- the prints the question,
- searches on google,
- prints the search result,
- reads it as output audio.

## Running with Docker
Make sure you have docker installed and that the Docker daemon is running.
- `docker build -t ask-google .`
- `docker run -it -p 5000:5000 ask-google`

### Restrictions
Requires python3+ and pip3+
On Docker, the input device should be added on run command, this is only posible for Unix. 
For Windows, no solution has been found YET.

If you want to run on Virtual Environment, for the dependency of the package PyAudio,
PortAudio wheel package should be installed.

### Discussions
Since this scrapping depends on how Google names the search results' classes, it is error-prone.
Online tutorials use some weird class names like `Xwk` or `3bp` or `M4s` etc but none of them is generic.
