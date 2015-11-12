from flask import Flask, render_template
import loremipsum
app = Flask(__name__)
app.config.from_object({'debug': True})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):

    parents = ['/']
    accumulated = ''
    for p in path.split('/'):
        if p:
            accumulated += '/' + p
            parents.append(str(accumulated))

    children = [('/{}/{}' if path else '/{}{}').format(path, i) for i in range(4)]

    return render_template('first.html',
                           parents=parents,
                           children=children,
                           title=loremipsum.generate_sentence(),
                           paragraphs=loremipsum.get_paragraphs(3))

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
