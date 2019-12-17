#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *

class SonarQubeCe(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_ce_activity(self, **kwargs):
        """
        获取tasks
        :param kwargs:
        componentId: Id of the component (project) to filter on
        status: Comma separated list of task statuses;SUCCESS,FAILED,CANCELED,PENDING,IN_PROGRESS
        type: Task type
        onlyCurrents: Filter on the last tasks (only the most recent finished task by project)
        :return:
        """
        resp = self.sonarqube._make_call('get', RULES_CE_ACTIVITY_ENDPOINT, **kwargs)
        data = resp.json()
        return data['tasks']

    def get_ce_component(self, component):
        """
        Get the pending tasks, in-progress tasks and the last executed task of a given component (usually a project).
        Requires the following permission: 'Browse' on the specified component.
        Either 'componentId' or 'component' must be provided.
        :param component:
        :return:
        """
        params = {'component': component}
        resp = self.sonarqube._make_call('get', RULES_CE_COMPONENT_ENDPOINT, **params)
        return resp.json()

    def get_ce_task(self, **kwargs):
        """
        获取task信息
        Give Compute Engine task details such as type, status, duration and associated component.
        Requires 'Administer System' or 'Execute Analysis' permission.
        :param kwargs:
        additionalFields: Comma-separated list of the optional fields to be returned in response.
        id: Id of task
        :return:
        """
        resp = self.sonarqube._make_call('get', RULES_CE_TASK_ENDPOINT, **kwargs)
        return resp.json()
