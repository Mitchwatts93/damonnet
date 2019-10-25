def eval_from_input(link):
    """Generate output from a sequence"""

    ### replace this bit with generating an output instead
    html_result = result_to_html(get_result(link))

    # Formatting in html
    html = ''
    html = addContent(html, header(
        'Sentiment Analysis', color='#FE9023'))
    html = addContent(html, box(html_result))
    return f'<div>{html}</div>'

def get_result(link):
    return None

def result_to_html(result):
    return None

def header(text, color='black'):
    """Create an HTML header"""
    raw_html = f'<h1 style="margin-top:12px;color: {color};font-size:54px"><center>' + str(
        text) + '</center></h1>'
    return raw_html


def box(text):
    """Create an HTML box of text"""
    raw_html = '<div style="border-bottom:1px inset black;border-top:1px inset black;padding:8px;font-size: 28px;">' + str(
        text) + '</div>'
    return raw_html


def addContent(old_html, raw_html):
    """Add html content together"""
    old_html += raw_html
    return old_html
