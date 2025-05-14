import typing as t
from typing import Dict, List, Tuple

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx_design.cards import CardDirective
from sphinx_design.shared import WARNING_TYPE,PassthroughTextElement,create_component,is_component,make_choice,margin_option,text_align, create_component, margin_option, padding_option


def setup_taggedcard(app: Sphinx):
    """
    Set up the `InfoCardDirective` composite web element.
    """
    app.add_directive("tagged-card", TaggedCardDirective)

class TaggedCardDirective(SphinxDirective):
    """A component, which is a container for cards in a single scrollable row."""

    has_content = True
    required_arguments = 0  # columns
    optional_arguments = 1
    option_spec = {
        "tags": directives.class_option,
        "outline": directives.class_option,
    }

    def run(self) -> List[nodes.Node]:
        """Run the directive."""
        self.assert_has_content()
        try:
            cols = str(1)#make_choice([str(i) for i in range(1, 13)])(
                # self.arguments[0].strip()
            # )
        except ValueError as exc:
            raise self.error(f"Invalid directive argument: {exc}")

        classes = ["sd-sphinx-override", "sd-tagged-card", f"sd-card-cols-{cols}", 'd-flex']
        classes += self.options.get("tags", [])
        for color in self.options.get("outline", []):
            classes.append(f"outline-{color}")

        container = create_component(
            "tagged-card",
            classes
            # ["sd-sphinx-override", "sd-tagged-card", f"sd-card-cols-{cols}", 'd-flex']
            # + self.options.get("tags", [])
            # + self.options.get("classes", []),
        )
        # print(self.options.get("tags", []))
        self.set_source_info(container)
        self.state.nested_parse(self.content, self.content_offset, container)
        for item in container.children:
            if not is_component(item, "card"):
                LOGGER.warning(
                    "All children of a 'card-carousel' "
                    f"should be 'card' [{WARNING_TYPE}.card]",
                    location=item,
                    type=WARNING_TYPE,
                    subtype="card",
                )
                break
        return [container]


def setup(app):
    app.connect("builder-inited", setup_taggedcard)