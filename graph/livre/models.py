from django.db import models


class Node(models.Model):
    entity = models.CharField(max_length=200)
    value = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[' + self.entity + '] ' + self.value


class Edge(models.Model):
    start_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='start_node')
    end_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='end_node')
    action = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        start = '[' + self.start_node.entity + '] ' + self.start_node.value
        end = '[' + self.end_node.entity + '] ' + self.end_node.value
        return start + ' --> ' + self.action + ' --> ' + end
