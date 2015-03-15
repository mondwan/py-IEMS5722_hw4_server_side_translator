# -*- coding: utf-8 -*-
"""
- `File`: server.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: An implementation for doing translation required by
  Assignment 4
"""


from flask import Flask
from flask import request
from flask import jsonify


class MissingWordsQueryException(Exception):
    """
    An exception indicates there is missing "words" in the query string
    """
    pass

# Instantiate Flask application
app = Flask('IEMS5722-HW4-Translator')


def config(config):
    """
    Allows other to customize how flask works

    Attribute:

    - `config`: dict

    Return:

    - `Class::Flask`
    """
    app.config.update(config)

    return app


@app.route("/")
def translate():
    """
    A handler for translating given english word which about digit to chinese
    character

    Return:

    - `JSON`

      .. code-block

        # message = isError ? reason : "OK"
        # output = isError ? '' : <TRANSLATION>
        {
            message: string,
            output: string,
        }
    """
    ret = {'message': 'OK', 'output': ''}

    try:
        # Get request words from query string
        words = request.args.get('words')

        # Raise exception if there is no such query defined
        if words is None:
            raise MissingWordsQueryException()

        # Define our lookup table
        myMap = {
            'zero': '零',
            'one': '一',
            'two': '二',
            'three': '三',
            'four': '四',
            'five': '五',
            'six': '六',
            'seven': '七',
            'eight': '八',
            'nine': '九',
            'ten': '十',
        }

        # Since there maybe more than one words, loop through those words
        for word in words.split(' '):
            # Translate word by look up values in our lookup table
            output = myMap[word]

            # Set word to be output if there are no records at first
            # Otherwise, append to the output string
            ret['output'] = output \
                if (len(ret['output']) == 0) \
                else '%s %s' % (ret['output'], output)

    except MissingWordsQueryException:
        # Setup error message
        ret['message'] = 'Missing "words" query string'
        ret['output'] = ''
    except KeyError:
        # Setup error message
        ret['message'] = 'Translation error for word |%s|' % word
        ret['output'] = ''

    # Encode ret in JSON format so that it prints a json string on the web
    return jsonify(**ret)

if __name__ == "__main__":
    # Put default configuration if running from shell
    config({
        'DEBUG': False,
    })

    # Kick things start
    app.run(host='0.0.0.0', port=8080)
