# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class QueryTradeIntentionUserListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'QueryTradeIntentionUserList','trademark')

	def get_End(self):
		return self.get_query_params().get('End')

	def set_End(self,End):
		self.add_query_param('End',End)

	def get_Begin(self):
		return self.get_query_params().get('Begin')

	def set_Begin(self,Begin):
		self.add_query_param('Begin',Begin)