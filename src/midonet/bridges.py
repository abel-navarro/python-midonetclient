# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Bridge(ResourceBase):

    def _bridge_uri(self, tenant_id, bridge_uuid):
        response, content = self.cl.tenants().get(tenant_id)
        response, routers =  self.cl.get(content['bridges'])
        return self._find_resource(routers, bridge_uuid)

    def create(self, tenant_id, name):
        response, content = self.cl.tenants().get(tenant_id)
        uri =  content['bridges']
        data = {"name": name}
        return self.cl.post(uri, data)

    def list(self, tenant_id):
        response, content = self.cl.tenants().get(tenant_id)
        uri =  content['bridges']
        return self.cl.get(uri)

    def update(self, tenant_id, bridge_uuid, name):
        bridge_uri = self._bridge_uri(tenant_id, bridge_uuid)
        data = {"name": name}
        return self.cl.put(bridge_uri, data)

    def get(self, tenant_id, bridge_uuid):
        bridge_uri = self._bridge_uri(tenant_id, bridge_uuid)
        return self.cl.get(bridge_uri)

    def delete(self, tenant_id, bridge_uuid):
        bridge_uri = self._bridge_uri(tenant_id, bridge_uuid)
        return self.cl.delete(bridge_uri)

    def peer_ports(self, tenant_id, router_uuid):
        response, bridge = self.get(tenant_id, router_uuid)
        uri =  bridge['peerPorts']
        return self.cl.get(uri)
