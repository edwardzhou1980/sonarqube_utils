#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *


class SonarQubeIssue(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_project_issues(self, componentKeys, branch, **kwargs):
        """
        获取指定项目的issues
        :param componentKeys:
        :param branch:
        :return:
        """
        params = {
            'additionalFields': '_all',
            'componentKeys': componentKeys,
            'branch': branch
        }
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.sonarqube._make_call('get', RULES_ISSUES_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for issue in response['issues']:
                yield issue

            if page_num >= 100:
                break

    def issue_assign(self, issue_keys, assignee):
        """
        分配issue
        :param issue_keys:
        :param assignee:
        :return:
        """
        params = {
            'assignee': assignee
        }
        if isinstance(issue_keys, list):
            for issue_key in issue_keys:
                params['issue'] = issue_key
                self.sonarqube._make_call('post', RULES_ISSUES_ASSIGN_ENDPOINT, **params)
        elif isinstance(issue_keys, str):
            params['issue'] = issue_keys
            self.sonarqube._make_call('post', RULES_ISSUES_ASSIGN_ENDPOINT, **params)

    def issue_set_severity(self, issue, severity):
        """
        Change severity.
        :param issue:
        :param severity:
        :return:
        """
        params = {
            'issue': issue,
            'severity': severity
        }
        self.sonarqube._make_call('post', RULES_ISSUE_SET_SEVERITY_ENDPOINT, **params)

    def issue_set_type(self, issue, type):
        """
        Change type of issue, for instance from 'code smell' to 'bug'.
        :param issue:
        :param type:
        :return:
        """
        params = {
            'issue': issue,
            'type': type
        }
        self.sonarqube._make_call('post', RULES_ISSUE_SET_TYPE_ENDPOINT, **params)

    def issue_add_comment(self, issue, text):
        """
        给issue加批注
        :param issue:
        :param text:
        :return:
        """
        params = {
            'issue': issue,
            'text': text
        }
        self.sonarqube._make_call('post', RULES_ISSUE_ADD_COMMENT_ENDPOINT, **params)

    def issue_delete_comment(self, comment):
        """
        给issue删除批注
        :param comment:
        :return:
        """
        params = {
            'comment': comment
        }
        self.sonarqube._make_call('post', RULES_ISSUE_DELETE_COMMENT_ENDPOINT, **params)

    def issue_edit_comment(self, comment, text):
        """
        更新comment
        :param comment:
        :param text:
        :return:
        """
        params = {
            'comment': comment,
            'text': text
        }
        self.sonarqube._make_call('post', RULES_ISSUE_EDIT_COMMENT_ENDPOINT, **params)

    def issues_do_transition(self, issue_keys, transition):
        """
        对指定项目的issues进行操作
        :param issue_keys:
        :param transition:
        :return:
        """
        params = {
            'transition': transition
        }
        if isinstance(issue_keys,list):
            for issue_key in issue_keys:
                params['issue'] = issue_key
                self.sonarqube._make_call('post', RULES_ISSUES_DO_TRANSITION_ENDPOINT, **params)
        elif isinstance(issue_keys,str):
            params['issue'] = issue_keys
            self.sonarqube._make_call('post', RULES_ISSUES_DO_TRANSITION_ENDPOINT, **params)

