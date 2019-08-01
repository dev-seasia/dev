from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics,serializers, status
from rest_framework.views import APIView
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.storage import SQLStorageAdapter
from chatterbot.trainers import ChatterBotCorpusTrainer
import json
from flask import Flask, render_template, request, jsonify
import os
from google import google
from pprint import pprint

class test(APIView):
    # chatterbot = ChatBot("Friday")
    chatterbot = ChatBot(
        'Friday',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'i am confused',
                'maximum_similarity_threshold': 0.90
            }
        ]
    )

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))
        if 'text' not in input_data:
            return Response({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)
        elif input_data['text'] == "quit":
            return Response({
                'text': [
                    'See you Later Sir. BYE!!'
                ]
            }, status=200)

        response = self.chatterbot.get_response(input_data)
        response_data = response.serialize()

        if response_data['text'] == "i am confused":
            string_for_google_Search = input_data['text'].replace(" ", "+")
            google_link = ' || more details - https://www.google.com/search?q='+string_for_google_Search
            search_results = google.search(input_data['text'])
            response_data['text'] = search_results[1].description + google_link

        return Response({
              'friday': response_data['text']
            # 'you :': response_data['in_response_to'],
            # 'Friday :': response_data['text']
        }, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return Response({
            'name': self.chatterbot.name
        })
