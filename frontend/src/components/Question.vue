<template>
    <div class="quest">
        <div class="formulation">{{ title }}</div>
        <div class="answer"><input :type="type" readonly value="Answer"></div>
        <button @click="$emit('remove')">Delete</button>
    </div>
</template>

<script>
export default {
    props:[
        'title',
        'type'
    ]
}
</script>