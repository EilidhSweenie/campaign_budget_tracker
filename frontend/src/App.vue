<script setup>
import {ref, reactive, watch} from 'vue'
  // Table items
  const items = [
    {
      name: 'Account A',
      budget: '£10000',
      spend: '£50',
      status: 'In Budget',
    },
    {
      name: 'Account B',
      budget: '£100',
      spend: '£50',
      status: 'Warning',
    },
    {
      name: 'Account C',
      budget: '£10',
      spend: '£50',
      status: 'Out of Budget',
    },
        {
      name: 'Account A',
      budget: '£10000',
      spend: '£50',
      status: 'In Budget',
    },
    {
      name: 'Account B',
      budget: '£100',
      spend: '£50',
      status: 'Warning',
    },
    {
      name: 'Account C',
      budget: '£10',
      spend: '£50',
      status: 'Out of Budget',
    },
        {
      name: 'Account A',
      budget: '£10000',
      spend: '£50',
      status: 'In Budget',
    },
    {
      name: 'Account B',
      budget: '£100',
      spend: '£50',
      status: 'Warning',
    },
    {
      name: 'Account C',
      budget: '£10',
      spend: '£50',
      status: 'Out of Budget',
    },
        {
      name: 'Account A',
      budget: '£10000',
      spend: '£50',
      status: 'In Budget',
    },
    {
      name: 'Account B',
      budget: '£100',
      spend: '£50',
      status: 'Warning',
    },
    {
      name: 'Account C',
      budget: '£10',
      spend: '£50',
      status: 'Out of Budget',
    },
        {
      name: 'Account A',
      budget: '£10000',
      spend: '£50',
      status: 'In Budget',
    },
    {
      name: 'Account B',
      budget: '£100',
      spend: '£50',
      status: 'Warning',
    },
    {
      name: 'Account C',
      budget: '£10',
      spend: '£50',
      status: 'Out of Budget',
    },
        {
      name: 'Account A',
      budget: '£10000',
      spend: '£50',
      status: 'In Budget',
    },
    {
      name: 'Account B',
      budget: '£100',
      spend: '£50',
      status: 'Warning',
    },
    {
      name: 'Account C',
      budget: '£10',
      spend: '£50',
      status: 'Out of Budget',
    }
  ]

  // Define headers
  const headers =[
    { title: 'Name', key:'name', align:'start' },
    { title: 'Budget', key:'budget' },
    { title: 'Spend', key:'spend'  },
    { title: 'Status', key:'status', align:'end', sortable: true }
  ]

  // Pop up form conditional 
  const dialog = ref(false)

  const formRef = ref(null)

  const submitted = ref(false)

  // Define form data
  const formData = ref({
    name:'',
    budget: '',
    spend:'',
    status:'In Budget'
  })

  
  const formErrors = reactive({
    name: '',
    budget: '',
    spend: '',
    status: ''
  })

  // Form rules
  const rules = {
    required: (value) => !!value || 'This field is required',
  }

  
  // Add new campaign button functionality 
  const addCampaign = () => {
    submitted.value = true
    // Checks if all fields are present
    formErrors.name = ''
    formErrors.budget = ''
    formErrors.spend = ''
    formErrors.status = ''

    let hasError = false
    if (!formData.value.name) { formErrors.name = 'Name is required'; hasError = true }
    if (!formData.value.budget) { formErrors.budget = 'Budget is required'; hasError = true }
    if (!formData.value.spend) { formErrors.spend = 'Spend is required'; hasError = true }
    if (!formData.value.status) { formErrors.status = 'Status is required'; hasError = true }

    if (hasError) return
    console.log('Form submitted', formData.value)
    items.push({ ...formData.value }) 
    dialog.value = false             
    formData.value = { name: '', budget: '', spend: '', status: 'In Budget' }
    formRef.value.resetValidation()
  }

  // Return expected colour based on status
  const getStatusColor = (status) => {
  switch (status) {
    case 'In Budget': return 'green'
    case 'Warning': return 'orange'
    case 'Out of Budget': return 'red'
    default: return 'grey'
  }
}

  watch(dialog, (newVal) => {
    if (!newVal) {
      submitted.value = false
      formErrors.name = ''
      formErrors.budget = ''
      formErrors.spend = ''
      formErrors.status = ''
      formData.value = { name: '', budget: '', spend: '', status: 'In Budget' }
    }
  })
</script>

<template>
  <v-app>
    <v-main>
      <!-- Table Container -->
      <v-container fluid>
        <v-sheet border rounded>
          <v-data-table 
            :headers="headers"
            :items="items"
            >
            <!-- Table header with add campaign button -->
            <template v-slot:top>
              <v-toolbar flat color="primary">
                <!-- Title -->
                <v-toolbar-title>
                  Current Campaigns
                </v-toolbar-title>

                <!-- Button -->
                <v-btn
                  class="yellow-btn me-2"
                  rounded="lg"
                  prepend-icon="mdi-plus"
                  border
                  @click="dialog = true"
                >
                Add Campaign
                </v-btn>
              </v-toolbar>
            </template>
            
            <!-- Render status on traffic light system based on status -->
            <template v-slot:item.status="{ item }">
              <v-chip :color="getStatusColor(item.status)">
                {{ item.status }}
              </v-chip>
            </template>
          </v-data-table>
        </v-sheet>    
      </v-container>

      <!-- Add Campaign Pop-up Form -->
      <v-dialog  v-model="dialog" max-width="500">
          <v-card>
            <!-- Title -->
            <v-card-text>
              Add New Campaign
            </v-card-text>

            <v-sheet class="mx-auto" width="300">
              <v-form ref="formRef" @submit.prevent>
                <v-text-field
                  v-model="formData.name"
                  label="Name"
                  :error="submitted && !!formErrors.name"
                  :error-messages="submitted ? formErrors.name : ''"
                ></v-text-field>
                <v-text-field
                  v-model="formData.budget"
                  label="Budget"
                  type="number"
                  :error="submitted && !!formErrors.budget"
                  :error-messages="submitted ? formErrors.budget : ''"
                  min="0"
                  step="1"
                ></v-text-field>
                <v-text-field
                  v-model="formData.spend"
                  label="Spend"
                  type="number"
                  :error="submitted && !!formErrors.spend"
                  :error-messages="submitted ? formErrors.spend : ''"
                  min="0"
                  step="1"
                ></v-text-field>
                <v-select
                  v-model="formData.status"
                  :items="['In Budget', 'Warning', 'Out of Budget']"
                  label="Status"
                  :error="!!formErrors.status"
                  :error-messages="formErrors.status"
                ></v-select>
              </v-form>
            </v-sheet>

            <v-card-actions>
              <v-spacer></v-spacer>
                <v-btn text="Add New Campaign" class=yellow-btn @click="addCampaign">Add</v-btn>
                <v-btn text="Close Dialog" class=yellow-btn @click="dialog = false">Cancel</v-btn> 
            </v-card-actions>
          </v-card>
      </v-dialog>
    </v-main>
  </v-app>
</template>
  

<style>
  .yellow-btn {
    background-color: #FFDD33; 
  }
  .yellow-btn .v-btn__content,
  .yellow-btn .v-icon {
    color: #000 !important;
  }
</style>
