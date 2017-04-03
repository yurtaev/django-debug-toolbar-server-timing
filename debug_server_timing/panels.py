from debug_toolbar.panels import Panel


class ServerTimingPanel(Panel):
    title = 'Server Timing'

    def generate_stats(self, request, response):
        sql_panel = self.toolbar.stats.get('SQLPanel')
        if sql_panel:
            num_queries = len(sql_panel.get('queries', []))
            sql_time = sql_panel.get('sql_time')
            response['Server-Timing'] = 'sql_time={}; "SQL {} queries"'.format(sql_time, num_queries)
