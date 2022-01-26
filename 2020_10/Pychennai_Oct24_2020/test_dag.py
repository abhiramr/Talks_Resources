# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from __future__ import print_function

import time
from builtins import range
from pprint import pprint

from airflow.utils.dates import days_ago

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

args = {
    'owner': 'Abhiram',
    'start_date': days_ago(0),
}

dag = DAG(
    dag_id='test_py_operator',
    default_args=args,
    schedule_interval=None,
    tags=['test']
)

def print_this():
    print("Time now is {}".format(datetime.now()))

def print_next():
    print("What is happening?")

# Generate 5 printing tasks, sleeping from 0.0 to 0.4 seconds respectively
task1 = PythonOperator(
    task_id='printer1',
    python_callable=print_this,
    dag=dag,
)
task2 = PythonOperator(
    task_id='printer2',
    python_callable=print_next,
    dag=dag,
)

task1 >> task2
