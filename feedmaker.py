#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Provides FeedMaker, a general and simple to use class for making RSS 2.0 xml
feeds. There is currently no documentation aside from the sample usage.


COPYLEFT NOTICE
---------------
Copyright 2016 David Lowry-Duda

Based on rss2producer, 2014.
rss2producer creator: nathan-osman
Nathan very kindly released rss2producer under MIT.

You are free to redistribute and/or modify FeedMaker under the
terms of the MIT License.

I'm happy if you find FeedMaker useful, but be advised that
it comes WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""


from xml.dom.minidom import Document

class FeedMaker(object):
    "An RSS 2.0 feed creater."

    class FeedError(Exception):
        "A Feed Exception"
        pass

    def __init__(self, title=None, link=None, description="", **kwargs):
        """
        Initialize the feed with the specified attributes.
        Each attribute is put in the RSS Channel data.
        """
        self._document = Document()

        rss_element = self._document.createElement('rss')
        rss_element.setAttribute('version', '2.0')
        self._document.appendChild(rss_element)

        self._channel = self._document.createElement('channel')
        rss_element.appendChild(self._channel)
        self._channel.appendChild(self._create_text_element('title', title))
        self._channel.appendChild(self._create_text_element('link', link))
        self._channel.appendChild(self._create_text_element('description', description))

        for kwarg, value in kwargs.items():
            self._channel.appendChild(self._create_text_element(kwarg, value))

    def _create_text_element(self, key, text):
        "Create and return text element."
        element = self._document.createElement(key)
        element.appendChild(self._document.createTextNode(text))
        return element

    def append_item(self, title=None, description=None, **kwargs):
        "Append item to the feed. Must contain either a title or a description."
        # Either title or description *must* be present
        if title is None and description is None:
            raise self.FeedError("A title or description must be provided.")

        element = self._document.createElement('item')

        # title and description are special in RSS2, so they are distinguished
        if not title is None:
            element.appendChild(self._create_text_element('title', title))
        if not description is None:
            element.appendChild(self._create_text_element('description', description))

        for kwarg, value in kwargs.items():
            element.appendChild(self._create_text_element(kwarg, value))

        self._channel.appendChild(element)

    def get_xml(self):
        "Return the XML for the feed."
        return self._document.toxml()
