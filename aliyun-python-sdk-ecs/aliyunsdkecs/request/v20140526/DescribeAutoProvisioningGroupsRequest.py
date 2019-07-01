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
class DescribeAutoProvisioningGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeAutoProvisioningGroups','ecs')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_AutoProvisioningGroupStatuss(self):
		return self.get_query_params().get('AutoProvisioningGroupStatuss')

	def set_AutoProvisioningGroupStatuss(self,AutoProvisioningGroupStatuss):
		for i in range(len(AutoProvisioningGroupStatuss)):	
			if AutoProvisioningGroupStatuss[i] is not None:
				self.add_query_param('AutoProvisioningGroupStatus.' + str(i + 1) , AutoProvisioningGroupStatuss[i]);

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_AutoProvisioningGroupIds(self):
		return self.get_query_params().get('AutoProvisioningGroupIds')

	def set_AutoProvisioningGroupIds(self,AutoProvisioningGroupIds):
		for i in range(len(AutoProvisioningGroupIds)):	
			if AutoProvisioningGroupIds[i] is not None:
				self.add_query_param('AutoProvisioningGroupId.' + str(i + 1) , AutoProvisioningGroupIds[i]);

	def get_AutoProvisioningGroupName(self):
		return self.get_query_params().get('AutoProvisioningGroupName')

	def set_AutoProvisioningGroupName(self,AutoProvisioningGroupName):
		self.add_query_param('AutoProvisioningGroupName',AutoProvisioningGroupName)