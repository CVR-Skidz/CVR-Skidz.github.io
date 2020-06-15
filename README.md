# [CVR-Skidz.github.io](https://CVR-Skidz.github.io)
A personal website hosted on github.

## Building
`build.py` is contained at the root of the project. This should be placed in the same directory as the hosted page, by default `index.html`. This script is run to build a single, static page. To build the contents of the file place an appropriate id in any component and create a directory of the same name. 

For example if I wanted to build a section of the page called "More":
```
<h1>More</h1>
<div id="More">
/* output here */
</div>
```
- `./More/` must exist.
- All files placed in the directory will be generated as children of the corresponding element.

### Content Folders
Folders supplied to the script, such as the example `./More/` should contain any files which contain the body of the children elements.

- The name of these file's are used as headings for each child element, and must be a valid public repository on github at the time of writing. These are automatically linked to the project page on github.
- Ommit file extensions for best results. E.g. `test.txt` --> `test`
- The contents of the file is placed under the heading.

### Usage
```
python build.py [paths-to-content]
```

Finally to stitch the contents of all files together run `build.py` supplying all content folders as arguments, space seperated. E.g. `python build.py ./More/ ./CRepos ./JavaRepos`
