from tagapp.models import Tag
from conspectapp.models import Conspect


def tagings(tags,user_id):
    tag_list = tags.split(", ")
    all_tags = Tag.objects.all()
    all_tags_list = []
    for tag in Tag.objects.values('name'):
        all_tags_list.append(tag['name'])
        print(all_tags_list)
    for new_tag in tag_list:
        if new_tag not in all_tags_list:
            s = Tag(name=new_tag, count=1)
            s.save()
        elif new_tag in all_tags_list:
            s = Tag.objects.get(name=new_tag)
            s.count += 1
            s.save()
        conspect = Conspect.objects.filter(author=user_id).order_by('-created')[0]
        conspect.tags.add(s)
