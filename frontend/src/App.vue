<script setup>
import {ref, reactive, watch, onMounted} from 'vue'
import axios from 'axios';

  // Table items
  const items = ref([]);

  // Define headers
  const headers =[
    { title: 'Name', key:'name', align:'start' },
    { title: 'Budget', key:'budget' },
    { title: 'Spend', key:'spend'  },
    { title: 'Status', key:'status', align:'end', sortable: true }
  ]

  // Initialise conditionals 
  const dialog = ref(false)

  const formRef = ref(null)

  const submitted = ref(false)

  // Map status code to chip colour, user friendly label and status code used in backend.
  const STATUS_MAP = {
    IN_BUDGET:{ label: 'In Budget',color: '#33FF5F'},
    WARNING:{label: 'Warning', color: '#FFDD33'},
    OUT_OF_BUDGET:{ label: 'Out of Budget', color: '#FF3333' },
  };

  const getStatusMeta = (statusValue) => {
    return STATUS_MAP[statusValue] || { label: statusValue, color: 'grey' };
  };

  const statusOptions = Object.entries(STATUS_MAP).map(([value, meta]) => ({
    value,
    label: meta.label,
  }));


  // Define form data
  const formData = ref({
    name:'',
    budget: '',
    spend:'',
    status:'IN_BUDGET'
  })

  // Define form errors
  const formErrors = reactive({
    name: '',
    budget: '',
    spend: '',
    status: ''
  })

  //Fetch Campaigns 
  const fetchCampaigns = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/campaigns/view/');
      items.value = response.data; 
    } catch (error) {
      console.error('Failed to fetch campaigns', error);
    }
  };

  onMounted(() => {
    fetchCampaigns();
  });

  // Form rules
  const rules = {
    required: (value) => !!value || 'This field is required',
  }

  // Add new campaign button functionality 
  const addCampaign = async () => {
    submitted.value = true

    formErrors.name = ''
    formErrors.budget = ''
    formErrors.spend = ''
    formErrors.status = ''

    let hasError = false
    if (!formData.value.name) { formErrors.name = 'Name is required'; hasError = true }
    if (!formData.value.budget) { formErrors.budget = 'Budget is required'; hasError = true }
    if (!formData.value.spend) { formErrors.spend = 'Spend is required'; hasError = true }
    if (!formData.value.status) { formErrors.status = 'Status is required'; hasError = true }

    if (hasError) return;

      try {
        await axios.post(
          'http://127.0.0.1:8000/campaigns/add/',
          formData.value
        );

        // Refresh Table
        await fetchCampaigns();

        // Reset Form
        formData.value = { name: '', budget: '', spend: '', status: 'In Budget' };
        submitted.value = false;
        dialog.value = false;
      } catch (error) {
          if (error.response) {
            console.error('Failed to add campaign', error.response.data);
          } else {
            console.error('Failed to add campaign', error);
          }
      }
    
  }

  // Reset popup values
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
              <v-chip 
                variant="flat"
                class="status-chip"
                :style="{ backgroundColor: getStatusMeta(item.status).color}">
                {{ getStatusMeta(item.status).label }}
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
                  :items="statusOptions"
                  item-title="label"
                  item-value="value"
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
  /* Button Styles */
  .yellow-btn {
    background-color: #FFDD33; 
  }
  .yellow-btn .v-btn__content,
  .yellow-btn .v-icon {
    color: #000 !important;
  }

  /* Chip Styling */
  .status-chip {
    border-radius: 8px !important; 
  }

  .status-chip .v-chip__content{
    color: #000 !important;      
  }
</style>
