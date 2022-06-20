# Python Implementation of Pixel Value Differencing based Steganography

LSB substitution and PVD are applied. In PVD, adaptive non-overlapping 3x3 pixel blocks or a combination of 3x3 and 2x2 blocks are used in raster fashion.

As of now extraxtion is done using the generated log file containing data locations in cover Image.

Source Code is documented.

**Only PNG Image** files should be used as cover image and final output image.

## Getting Started

Clone repository.

### Prerequisites

- python3
- Python Image Library (PIL)

## Usage: Embedding

> Usage: python3 pvdEmbed.py i/p_File Cover_Image 

> Eg:    python3 pvdEmbed.py enc test.png 

> Embed data Log can be found as: embedlog.log

## Usage: Extraction

> Usage: python3 pvdExtract.py Embedded_Cover_Image_File Output_File 

> Eg:    python3 pvdExtract.py protest.png cipher

## Author

* **Tony Josi** - [TonyJosi97](https://github.com/TonyJosi97)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


