This project builds a Markov chain from your Facebook message history

**Requires Python 3**

## 1. Installing Dependencies
1. `pip3 install markovify`

## 2. Creating the corpus

1. Go to Facebook's [download your information](https://www.facebook.com/settings?tab=your_facebook_information) page
2. Click "View" next to "Download your information"
2. Set Format to JSON, Media quality to low and only check Messages. Click 'Create File'
3. Once your file has been created (this will take some time), download and unzip it
4. Place the `messages` directory into the root of this project
5. Run `python3 concat-messages.py`
6. Run `python3 generate-corpus.py`

## 3. Generating Messages

1. Run `python3 generate-sentences.py`

You can edit this file to change the number of messages it generates at once.