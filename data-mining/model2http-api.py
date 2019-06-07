import tensorflow as tf
def save_model_to_serving(model, export_version, export_path='model/'):
    print(model.input, model.output)
    signature = tf.saved_model.signature_def_utils.predict_signature_def(                                                                        
        inputs={'img_input': model.input[0], # mutil input support
                'extra_input': model.input[1], 
               }, 
        
        outputs={'outputs': model.output}
    )
    export_path = os.path.join(
        tf.compat.as_bytes(export_path),
        tf.compat.as_bytes(str(export_version)))
    builder = tf.saved_model.builder.SavedModelBuilder(export_path)
    legacy_init_op = tf.group(tf.tables_initializer(), name='legacy_init_op')
    builder.add_meta_graph_and_variables(
        sess=K.get_session(),                                                                                                                    
        tags=[tf.saved_model.tag_constants.SERVING],                                                                                             
        signature_def_map={                                                                                                                      
            'serving_default': signature,                                                                                                                     
        },
        legacy_init_op=legacy_init_op)
    builder.save()
save_model_to_serving(good_naive, "1", './save_to_serving') # save to different directory according to the second params indicating version

import requests
import json
payload = {
    "instances": [
        {
        "img_input": img_input_1.tolist(), #x_val[0][0].tolist(),
        "extra_input": extra_input_1.tolist(), # x_val[1][0].tolist(),
    }
    ]
}
url = 'http://example.com/predict'
r = requests.post(url, json=payload)
pred = json.loads(r.content.decode('utf-8'))
pred
