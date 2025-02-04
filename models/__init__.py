from tortoise import Model, fields


class StrategyExecInfo(Model):
    
    id = fields.CharField(pk=True, max_length=255)
    strategy_name = fields.CharField(max_length=255)
    completed = fields.CharField(max_length=1)
    start_time = fields.DatetimeField()
    # profit = fields.DecimalField(max_digits=30, decimal_places=8)
    # created_at = fields.DatetimeField(auto_now_add=True)
    # updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "strategy_exec_info"
        managed = False
        