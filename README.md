# Garyfallidis Research Group

## Background

This site makes use of [Sphinx](https://www.sphinx-doc.org/en/stable/) built via [PYData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/).

## Index

- `_static`: Contains all assets (images, CSS, JS) for Sphinx to look at.
- `_templates`: Contains html layout for custom Sphinx design.
- `_build`: Contains the generated documentation.
- `posts`: Contains all blog posts.
- `context`: Contains all the content management information

## Testing Locally: Doc generation steps:

### Installing requirements

To set up your computer to run this site locally, you need to install the various Python packages in the [requirements.txt](requirements.txt) at the top level of this repository.

```bash
$ pip install -U -r requirements.txt
```

### Generate all the Documentation

#### Under Linux and OSX

```bash
$ make -C . clean && make -C . html
```

#### Under Windows

```bash
$ ./make.bat clean
$ ./make.bat html
```

This will build a collection of html pages under `_build/html` and you can open the `index.html` using your browser of choice.
