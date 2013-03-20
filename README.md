jamespjh-wsd
============

Web sequence diagram command line tool

Based on content from http://www.websequencediagrams.com/embedding.html
With added ability to use your API key, and command line interface

Setup:

    sudo python setup.py install
    mkdir ~/.wsd # optional
    vim ~/.wsd/config.yml # Add key : yourkey, optional

Usage:

python -m websequence --in $SOURCE --out $TARGET [--style napkin]

Issues:

As yet, doesn't handle API errors, exits clean with problem.
