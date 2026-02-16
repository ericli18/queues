Showing how queues work

1. CPU scheduling

[Linux code](https://github.com/torvalds/linux/blob/master/kernel/sched/core.c)

```c
/*
 * Find left-most (aka, highest priority) and unthrottled task matching @cookie.
 * If no suitable task is found, NULL will be returned.
 */
static struct task_struct *sched_core_find(struct rq *rq, unsigned long cookie)
{
	struct task_struct *p;
	struct rb_node *node;

	node = rb_find_first((void *)cookie, &rq->core_tree, rb_sched_core_cmp);
	if (!node)
		return NULL;

	p = __node_2_sc(node);
	if (!sched_task_is_throttled(p, rq->cpu))
		return p;

	return sched_core_next(p, cookie);
}
```
