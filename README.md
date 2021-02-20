# Bob_Ross_Paintings

This repo contains my attempt to use my full breadth of data science techniques to perform a deep dive into a classic show that has cemented itself into television history of a bygone era. 
The data provided in this repo is a structured combination of multiple sources in order to create a comprehensive look at Bob Ross's [*The Joy of Painting*](https://en.wikipedia.org/wiki/The_Joy_of_Painting)  

Official Bob Ross Youtube channel: [BobRossInc](https://www.youtube.com/user/BobRossInc)

![Bob Ross Image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS117A8XFP17_8SGyMZ_k8ne_nS1Ls0nqXagUc_F2lgbxilRYZqQQ&s)


# Repo Structure  
The following section of the README will outline the structure of this repo  

## data/  

`bob_ross_paintings.csv`  
.csv file containing metadata for each painting.

| Column | Description | Data Type |
|---|---|---|
| `painting_index` | Painting number as enumerated in collection. | number |
| `img_src` | Url path to image. | text |
| `painting_title` |  Title of the painting. | text |
| `season` | Season of 'The Joy of Painting' in which the painting was featured. | number |
| `episode` | Episode of 'The Joy of Painting' in which the painting was featured. | number |
| `num_colors` | Number of unique colors used in the painting. | number |
| `youtube_src` | Youtube video of episode featuring the painting. | text |
| `colors` | List of colors used in the painting. | list |
| `colors_hex` | List of colors (hexadecimal code) used in the painting. | list |  

=====================================================================  


`bob_ross_air_dates.csv`  
.csv file containing the episode title and air date of each episode  

| Column | Description | Data Type |
|---|---|---|
| `ep_info` | String containing ep. title and original air date | text |  

=====================================================================


## data/paintings/

Directory with a `.png` image for each painting. The file names correspond to the `painting_index` number as recorded in the `bob_ross_paintings.csv`.

## data/transcripts/

Directory of `.txt` files containing Closed Caption transcriptions for each episode.   
The text files are titled based on their YouTube videoID, which can be found in the `bob_ross_paintings.csv`.  
If no transcript is avaiable for the episode, it is noted in the file name and the file's contents.  
___
## scripts/

`get_bob_ross_paintings.py`

Python script used to scrape the paintings from http://twoinchbrush.com/

Example use:

```
# call without arguments
$ python get_bob_ross_paintings.py

# call with arguments
$ python get_bob_ross_paintings.py  --csv_name bobross.csv --verbose 1
```


`dl_images.sh`

Shell script that, when run, will download a `.png` for each painting and save it in `data/paintings/`.

Example use:

```
# call without arguments
$ bash dl_images.sh
```
___
## notebooks/  

`Painting Analysis.ipynb`  
Jupyter Notebook  that contains data cleaning, engineering, and temporarily transcription download functions.
