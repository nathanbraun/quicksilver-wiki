
# Metaweb:Image use policy

From the Quicksilver Metaweb.

For the basics of using images, see also [Metaweb:How to edit a page](/metaweb-how-to-edit-a-page).



|  |
| --- |
| **Table of contents** showTocToggle("show","hide") |
| 
[1 Rules of thumb](/) 


[2 Copyright](/) 


[3 Editing Images](/) 


[4 Deleting Images](/) 


[5 Image titles](/) 


[6 Format](/) 


[7 Markup](/) 


[8 Size](/) 


[8.1 Resizing](/) 


[9 Revision history of articles containing images](/) 


[10 Recommended software](/) 
 |


## Rules of thumb


Here's a quick checklist of rules for use of images. After the list, a more detailed discussion explains the reasoning behind them. 

1. Keep copyrights in mind when uploading images.
2. **Use a clear, detailed, title**
3. Most images should be 150-250 pixels wide.
4. Crop the images to show just the relevant subject.
5. If you create images yourself or modify them (maps, diagrams etc.) upload also a version without any text. It will help other Wikipedias use them (translate them).
6. Don't put photo credits in articles or on the images themselves; put them on the description page.
7. Use JPEG format for photographic images, with moderate quality settings.
8. Use PNG or GIF format for icons, drawings, maps, flags, and such, unless you only have a JPEG original.
9. Add good alt text.


## Copyright



When you upload an image, make sure you own the image, or that it is in the public domain, or that the copyright holder has agreed to license it under the GFDL. Please note its copyright status on the image description page.

Under United States copyright law, all images that were **published** before January 1, 1923 in the United States are now in the public domain, but this does not apply to images that were created prior to 1923 and **published** in 1923 or later. The year 1923 has special significance and this date does not roll forward in 2004.
This is particularly significant because Metaweb pages are currently hosted on a server in the United States.

## Editing Images


To replace an image with an edited version, use the [Upload file](/special-upload) page, and make sure that your file has the same name as the one that you want to replace. Converting an image to another file format the (end of) the image name changes, hence one gets a separate image description page.

## Deleting Images



1. Drop a line to the person who uploaded the image, telling them of your concerns. You may be able to resolve the issue at this point.
2. remove all uses of the image from articles - make it an [orphan](/metaweb-orphan)
3. add the [listed for deletion notice](/metaweb-deletion-policy) to the image description page.
4. The image can then be deleted after a week.


To actually delete an image after following the above procedure, you must be an [administrator](/metaweb-administrators). To do so, go to the image description page and click the *(del)* link. Do *not* click the *Delete this page* link, as this will delete the image description page but leave the image intact. To delete the image talk page (if any), you can use the *Delete this page* link as usual. **Deleted images cannot be undeleted!** Therefore they are gone permanently unless someone happened to keep a backup.

## Image titles


Descriptive titles are also useful. Uploading a file named, for example, "Africa.png" is likely to collide with one already present, and doesn't give any clue about its contents. A more descriptive name like "Africa\_map\_2002.png" is better. Avoid special characters in filenames or excessively long filenames, though, as that might make it difficult for some users to download the files onto their machines.

If you make an improved version of the same image - perhaps a scanned image that you scanned again with a better quality scanner, or you used a better way of reducing the original in scale - then upload it with the same title as the old one. This allows people to easily compare the two images, and avoids the need to delete images or change articles. However, this is not possible if the format is changed, since then at least the extension part of the name has to be changed.

Currently there is no easy way to rename an image - you have to just save it and re-upload it.

## Format


* Drawings, icons, political maps, flags and other such images (basically those with large,simple,and continuous blocks of color) should be in PNG or GIF format.
* Photos and photo-like maps should be in JPEG format.
* Animations should be in animated GIF format.


In general, if you have a good image that is in the wrong format, convert it to the correct format before uploading. However, if you find a map, flag, etc in JPEG format, only convert it to PNG if this reduces the file size without causing artifacts. 

Try to avoid cropping or otherwise editing JPEGs too frequently--each edit creates more loss of quality. If you can find an original of a photograph in 16-bit or 24-bit PNG or TIFF, edit that, and save as JPEG before you upload.

Avoid images that mix photographic and iconic content.
Though Cascading Style Sheets (CSS) makes it easy to use a PNG overlay on top of a JPEG image, the Wikipedia software does not allow such a technique. Thus, both parts must be in the same file, and the quality of one or the other will suffer.

## Markup


Here are some examples of typical markup ("**image**" for an image in the page, "**media**" for just a link):



|  |  |
| --- | --- |
| left float, no caption | `<div style="float:left;margin:0 1em 1em 0;">[[Image:NAME|Alt text]]</div>` |
| right float, no caption | `<div style="float:right;margin:0 0 1em 1em;">[[Image:NAME|Alt text]]</div>` |
| left float, with caption | `<div style="float:left;margin:0 1em 1em 0;text-align:center;">[[Image:NAME|Alt text]]<br>''Caption''</div>` |
| right float, with caption | `<div style="float:right;margin:0 0 1em 1em;text-align:center;">[[Image:NAME|Alt text]]<br>''Caption''</div>` |
| left float, with larger | `<div style="float:left;margin:0 1em 1em 0;text-align:center;">[[Image:SMALL|Alt text]]<br>[[Media:LARGE|larger version]]</div>` |
| right float, with larger | `<div style="float:right;margin:0 0 1em 1em;text-align:center;">[[Image:SMALL|Alt text]]<br>[[Media:LARGE|larger version]]</div>` |
| large central picture | `<center>[[Image:NAME|Alt text]]<br>''Caption''</center>` |



If your caption is longer than a few words, you may need to explicitly set the `div` width. Some browsers adjust the width of the `div` based on the width of the text, and if there is a large caption, the `div` may become too large. To solve this problem, simply set the width of the `div` to the width (in pixels) of the image, like so:

`<div style="width: 250px; float:right; margin:0 0 1em 1em; text-align: center;">[[image:NAME|alt text]]<br>''Caption''</div>`

(replacing `width: 250px;` with the correct width of your image. The inclusion of this specification is optional, but recommended if you have a caption longer than a few words. For large amounts of caption text, use `text-align:left;` to make it left-justified.

Alternate text is optional but recommended.

To have some text to the left of an image, and then some more text below the image, then put in a single <br clear="all">. This will force following text down until the margins are free of floating images.

## Size


Scale and crop images to a size appropriate for the article. Keep in mind that many readers are using 800x600 displays, and so images wider than 300-400 pixels may overwhelm the article. Larger images also take more time to download over slow links. Likewise, images smaller than 100 pixels wide may be difficult for users of larger displays to see. An optimum size for images with text flowing around them would be 150-250 pixels. Images without text on the side can be wider.

Of course image complexity is an important factor to consider when sizing images. Don't use tiny "thumbnail" images linked to a large image--use an
image of the appropriate size; adding a link to a larger version (perhaps the original source) is fine as well, but don't upload the larger one unless it is really needed.

### Resizing


When resizing large pictures to smaller ones:
* Crop out unimportant background.
* Please preserve the original aspect ratio, streched images look non-proportional and confusing.
* Consider using an integer ratio such as 1:2 or 1:3, which may produce better results.
* Resize from the largest resolution available - if you have a 2048pixel version, work from that, not the 800pixel version uploaded.
* Consider file size as well as image size - sometimes a version with more pixels but fewer bytes is preferable.
* Consider using the most advanced resample filter (such as Lancoz, B-Spline etc.) this will render the smaller image in the highest quality possible and will avoid artifacts such as aliasing or color reduction.
* When making a thumbnailed version to replace someone else's (presumably inferior) thumbnail, please keep the same name as the original.


## Revision history of articles containing images


Old versions of articles do not show corresponding old versions of images, but the latest ones, unless the file names of the images have changed.

## Recommended software


* Adobe Photoshop
* The [GIMP](/http-www-gimp-org)
* [ImageMagick](/http-www-imagemagick-org)
* [PMView](/http-www-pmview-com)
* [GraphicConverter](/http-lemkesoft-de-us-gcabout-html) (for Macs)
* [Irfanview](/http-www-irfanview-com), a multi-featured freeware tool, supports many image formats.



*This page originally from the [Wikipedia](/http-www-wikipedia-org).*
