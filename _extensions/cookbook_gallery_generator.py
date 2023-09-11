from gallery_generator import build_from_repos, generate_menu, generate_repo_dicts
import csv
import os
import yaml

def main(app):
    print(os.getcwd())
    # with open("cookbook_gallery.txt") as fid:
    #     all_items = fid.readlines()

    with open('cookbook_gallery.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        all_items = [row for row in reader]

    repo_dicts = generate_repo_dicts(all_items)

    title = "Cookbooks Gallery"

    subtext = ""
    with open("doc/cookbook_gallery_subtext.rst") as fid:
        for line in fid:
            subtext = subtext + line

    submit_btn_link =None# "https://github.com/ProjectPythia/cookbook-gallery/issues/new?assignees=ProjectPythia%2Feducation&labels=content%2Ccookbook-gallery-submission&template=update-cookbook-gallery.yaml&title=Update+Gallery+with+new+Cookbook"
    submit_btn_txt = None#"Submit a new Cookbook"
    menu_html = generate_menu(
        repo_dicts, submit_btn_txt=submit_btn_txt, submit_btn_link=submit_btn_link
    )
    print('build menu')
    build_from_repos(
        repo_dicts, "doc/gallery", title=title, subtext=subtext, menu_html=menu_html
    )


def setup(app):
    app.connect("builder-inited", main)
