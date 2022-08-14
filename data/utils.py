from datetime import datetime


def timer_save():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def sending_values():
    list_items = [a,b,c,d,e,f,g,h,i,j] 
    values_slave_list = []
    values_master_list = []
    i=0
    values = {}

    a={'slave_data':{'x':0.00,'y':0.00,'z':0.00,'strain':31,'rain':1}, 'maste_data':{'x':0.56,'y':14.78,'z':6.50,'strain':30,'temp':28.00,'humidity':67.40}}
    b={'slave_data':{'x':0.00,'y':0.00,'z':0.00,'strain':31,'rain':0}, 'maste_data':{'x':0.48,'y':14.74,'z':6.45,'strain':30,'temp':28.00,'humidity':67.40}}
    c={'slave_data':{'x':0.00,'y':0.00,'z':0.00,'strain':31,'rain':1}, 'maste_data':{'x':0.56,'y':14.76,'z':6.44,'strain':30,'temp':28.00,'humidity':67.40}}
    d={'slave_data':{'x':0.00,'y':0.00,'z':0.00,'strain':31,'rain':1}, 'maste_data':{'x':0.60,'y':14.76,'z':6.44,'strain':30,'temp':28.00,'humidity':67.40}}
    e={'slave_data':{'x':0.00,'y':0.00,'z':0.00,'strain':31,'rain':1}, 'maste_data':{'x':0.60,'y':14.77,'z':6.42,'strain':30,'temp':28.00,'humidity':67.40}}
    f={'slave_data':{'x':0.00,'y':0.00,'z':0.00,'strain':31,'rain':1}, 'maste_data':{'x':0.53,'y':14.74,'z':6.43,'strain':30,'temp':28.00,'humidity':67.40}}
    g={'slave_data':{'x':0.00,'y':0.00,'z':0.00,'strain':31,'rain':1}, 'maste_data':{'x':0.56,'y':14.80,'z':6.37,'strain':30,'temp':28.00,'humidity':67.40}}
    h={'slave_data':{'x':0.00,'y':0.00,'z':0.00,'strain':31,'rain':1}, 'maste_data':{'x':0.54,'y':14.73,'z':6.38,'strain':30,'temp':28.00,'humidity':67.40}}
    i={'slave_data':{'x':0.00,'y':0.00,'z':0.00,'strain':31,'rain':1}, 'maste_data':{'x':0.58,'y':14.76,'z':6.41,'strain':30,'temp':28.00,'humidity':67.40}}
    j={'slave_data':{'x':0.00,'y':0.00,'z':0.00,'strain':31,'rain':0}, 'maste_data':{'x':0.58,'y':14.74,'z':6.35,'strain':30,'temp':27.90,'humidity':67.30}}
    

    while(list_items):
        for v_id, v_info in values.items(list_items[i]):
            for key in v_info:
                if v_id == 'slave_data':
                    values_slave_list.append(v_info[key])
                else:
                    values_master_list.append(v_info[key])
        i = i + 1
    
    return values_slave_list, values_master_list