"""
Configuration of vocabulary game server.
Generated Sat Oct 22 19:08:48 PDT 2016
Edit to fit development or deployment environment.

"""

PORT=5000
DEBUG = True  # Set to False for production use
secret_key="2c02b708cf32cbaa37ab31117de155cf"
success_at_count = 3  # How many matches before we declare victory? 
vocab="data/vocab.txt"  # CHANGE THIS to use another vocabulary file

