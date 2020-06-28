import json

import requests
from celery.schedules import crontab
from celery.task import periodic_task

from lxml import etree

from document.models import ParsedFiles, LostDocument, DocumentType


@periodic_task(run_every=crontab(minute=0, hour='18'))
def my_parser():
    response = requests.get("https://data.gov.ua/dataset/ab09ed00-4f51-4f6c-a2f7-1b2fb118be0f")
    parser = etree.HTMLParser()
    data_set = etree.fromstring(response.text, parser)
    elements = data_set.xpath('/html/body/div[1]/div[2]/div/div[2]/div/article/div/section[1]/ul/li')
    for element in elements:
        href = str(element.xpath('*//ul/li[2]/a/@href')[0])
        if 'shema' in href:
            continue
        if ParsedFiles.objects.filter(file_id=element.xpath('@data-id')).exists():
            continue

        href = str(element.xpath('*//ul/li[2]/a/@href')[0])
        documents = json.loads(requests.get(href).text)

        docs = (
            LostDocument(
                identifier=d['ID'],
                series=d['D_SERIES'],
                number=d['D_NUMBER'],
                document_type=DocumentType.objects.get_or_create(name=d['D_TYPE'])[0],
                status=d['D_STATUS'],
                event_date=d['THEFT_DATA'],
                date_recorded=d['INSERT_DATE'],
                event_registration_authority=d['OVD']
            )
            for d in documents)

        LostDocument.objects.bulk_create(docs, ignore_conflicts=True, batch_size=5_000)
        ParsedFiles.objects.create(file_id=element.xpath('@data-id'))
        break
