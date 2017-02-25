
feedmaker
=========

This is a simple RSS 2.0 feed maker in python3. This relies on minidom to generate the xml.

This was based on the earlier [rss2producer](https://github.com/nathan-osman/rss2producer) by nathan-osman, who generously licensed his work under the MIT license. This version works with python3 (and accepts some nonstandard RSS 2 elements for minor abuse).


### Usage

Once installed, you can import the `RSS2Feed` class with the following line:

    from feedmaker import FeedMaker

To create a feed, simply use the `FeedMaker` constructor:

    feed = RSS2Feed(
        title='A Simple Title',
        link='http://example.org',
        description='A longer description of the feed contents.'
    )

After the feed is created, you can add items with the `append_item` method:

    feed.append_item(
        title='Sample Item',
        link='http://example.org/sample-item',
        description='A longer description of the sample item.',
        pub_date=datetime.utcnow()
    )

`FeedMaker` also accepts non-standard RSS2 items, and will create corresponding
XML.

When all of the items have been added to the feed, the XML contents can be
obtained with:

    feed.get_xml()

### Used in

`FeedMaker` is used in [hnrss](https://github.com/davidlowryduda/hnrss), an unofficial HackerNews RSS maker.
