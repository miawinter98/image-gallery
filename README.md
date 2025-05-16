# image-gallery

The easy-to-use image repository template tool... generator? Thing?

This tool is intended for the use case of people having a bunch of images they want to throw onto a static web page
for other people to see and access 

## How To

1. Fork / use this repository template for your own repository
2. Go into src/images and place all your images and associated meta files (more on that on the meta file section)
3. Activate GitHub Pages with the Actions Workflow and the default astro template, and you are good to go

## Meta files

For an image to be added to the page, it needs a meta file (.json). The meta file can look like this:

```
{
  "image": "./hamburg_by_mia_winter.jpg",
  "title": "Hamburg",
  "author": "Mia Rose Winter",
  "src": "https://miawinter.de/img/hamburg_by_mia_winter.jpg",
  "description": "A river canal in the German city of Hamburg, with adjacent houses on both sides",
  "license": "cc by-sa",
  "tags": [
    "Hamburg",
    "Huawei P40"
  ]
}
```

* `image` (required): the path to the associated image. Needs to be a valid path
* `title`: A title to be displayed above the image. Can be any string
* `author`: The name of that images author / creator. Can be any string
* `src`: The website where that image (and author) can be found. Will link on the Author name. Can be any URL
* `description`: An image description, used for alt-attributes. Can be any string
* `license`: The License under which that image is published. 
  Refer to [CC Licenses](https://creativecommons.org/share-your-work/cclicenses/). May be any string but CC
  terms are parsed as neat little svg images
* `tags`: A list of tags to assign to that image, will be rendered as little badges

As you can see anything but "image" is optional.

## Meta file tool

If you have a lot of images that for example you shot yourself and just want to publish quickly, there is a tool to 
help you create a batch of meta files with the same author / license. In the `src/images` folder you find the python 
script `batch-create.py`. It can be run using python 3.8 and requires no additional libraries. You can use it as 
follows:

`py batch-create.py ./foldername`

where the folder name is relative to the terminal location, which is in the `src/images` folder. Running this creates 
a .meta.json file for any image in that folder with the "image" property populated, making it show up on the page. You
can add additional properties like author with `--author` or license with `--license` like so:

`py batch-create.py ./foldername --author Mia Rose Winter --license CC BY-SA`

run `--help` for a list of all supported command line arguments

## Configuration

Some settings for the generated page, like the title of it, can be adjusted in the `src/config.yml` file

## Build without GitHub Pages

In case you want to use some other deployment tech, here is how the project itself is build:

1. Running `npm run build` using node 20 or later
2. Serving folder `dist`

## License

This repository is licensed under EUPL 1.2